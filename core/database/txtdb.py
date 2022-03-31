import os


class TxtDB:
    def __init__(self, filepath):
        self.filepath = filepath
        self.txtfile = open(filepath, "w+")

    def read(self):
        items = []
        for line in self.txtfile:
            stripped_line = line.strip()
            line_list = stripped_line.split()
            items.append(str(line_list[0]))

        return list(dict.fromkeys(items))

    def write(self, lst):
        # Appending function
        has_data = self.read()
        if (has_data):
            lst = list(dict.fromkeys(has_data + lst))

        with open(self.filepath, 'w') as f:
            for item in lst:
                f.write("%s\n" % item)

    def delete_line(self, lst):
        read = self.read()
        for l in lst:
            read.remove(l)

        os.remove(self.filepath)
        with open(self.filepath, 'w') as f:
            for item in read:
                f.write("%s\n" % item)

    def close(self):
        self.txtfile.close()
