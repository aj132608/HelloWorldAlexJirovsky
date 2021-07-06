class HelloWorld:
    def hello(self, num):
        message = ""

        for _ in range(num):
            message += "hello world!"

        return message


if __name__ == '__main__':
    hw_obj = HelloWorld()
    print(hw_obj.hello(2))
