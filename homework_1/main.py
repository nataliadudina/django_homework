from http.server import BaseHTTPRequestHandler, HTTPServer

host = 'localhost'
server_port = 8080


class MyServer(BaseHTTPRequestHandler):
    """ Специальный класс, который отвечает за обработку HTTP-запросов от клиентов """

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """

        if self.path == '/':
            file_path = 'index.html'
            try:
                with open(file_path, 'r') as file:
                    page_content = file.read()
                    self.send_response(200)  # Отправка кода ответа
                    self.send_header("Content-type", "text/html")  # Отправка типа данных, который будет передаваться
                    self.end_headers()  # Завершение формирования заголовков ответа
                    self.wfile.write(bytes(page_content, "utf-8"))  # Тело ответа
            except FileNotFoundError:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(bytes("File not found", "utf-8"))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(bytes("Page not found", "utf-8"))


if __name__ == '__main__':

    """
    Инициализация веб-сервера, который по заданным параметрам в сети
    принимает запросы и отправляет их на обработку специальному классу MyServer.
    """
    webServer = HTTPServer((host, server_port), MyServer)
    print("Server started http://%s:%s" % (host, server_port))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    print("Server stopped.")
