#include <poppler-document.h>
#include <poppler-page.h>
#include <poppler-page-renderer.h>
#include <iostream>

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Uso: " << argv[0] << " <arquivo_pdf>" << std::endl;
        return 1;
    }

    std::string arquivo_pdf = argv[1];
    poppler::document* documento = poppler::document::load_from_file(arquivo_pdf);
    if (!documento) {
        std::cerr << "Erro ao abrir o PDF." << std::endl;
        return 1;
    }

    for (int i = 0; i < documento->pages(); ++i) {
        poppler::page* pagina = documento->create_page(i);
        if (pagina) {
            std::string texto = pagina->text().to_latin1();
            for (char c : texto) {
                std::cout << c;
            }
            delete pagina;
        }
    }

    delete documento;
    return 0;
}