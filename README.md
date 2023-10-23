# OPIS PROGRAMU: służy do pobierania zawartości strony internetowej i wydobywania określonych elementów z użyciem wyrażenia XPath. Oto opis programu:

## Importowanie niezbędnych modułów:

click: To moduł do obsługi wiersza poleceń, który umożliwia uruchomienie programu z argumentami z linii poleceń.
lxml.html: To moduł, który pozwala na przetwarzanie HTML przy użyciu wyrażeń XPath.
requests: Moduł służący do wykonywania zapytań HTTP.
Funkcja extract(page_content, xpath): Ta funkcja przyjmuje zawartość strony i wyrażenie XPath jako argumenty. Wewnątrz funkcji, zawartość strony jest przetwarzana za pomocą lxml w celu znalezienia elementów, które pasują do wyrażenia XPath. Następnie tekst tych elementów jest wyodrębniany, usuwane są nadmiarowe białe znaki i znaki nowego wiersza, a wynik jest zwracany jako lista elementów.

Deklaracja funkcji main(url, xpath): Ta funkcja jest dekorowana przy użyciu click.command(), co oznacza, że program może być uruchamiany z wiersza poleceń. Przyjmuje dwa argumenty: url (adres strony internetowej) i xpath (wyrażenie XPath).

Wewnątrz funkcji main(), program rozpoczyna od pobrania zawartości strony, używając biblioteki requests. Następnie używa funkcji extract(), aby wydobyć elementy, które pasują do podanego wyrażenia XPath.

Ostatecznie znalezione elementy są wyświetlane na konsoli.

Warunek if __name__ == "__main__": sprawdza, czy program jest uruchamiany jako plik główny, a jeśli tak, to uruchamia funkcję main().

### Aby uruchomić ten program, musisz podać adres URL i wyrażenie XPath jako argumenty, na przykład:
python program.py "https://www.example.com" "//div[@class='example']/p"
Program pobierze zawartość strony o podanym adresie URL, a następnie wydobędzie i wyświetli wszystkie elementy ze strony. 
