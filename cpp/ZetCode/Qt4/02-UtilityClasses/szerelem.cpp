#include <QtCore/QTextStream>
#include <QtCore/QFile>


int main() {
    QFile data("szerelem.txt");
    QString line;

    if (data.open(QFile::ReadOnly)) {
        QTextStream in(&data);
        QTextStream out(stdout);

        out.setCodec("UTF-8");
        in.setCodec("UTF-8");

        do {
            line = in.readLine();
            out << line << endl;
        }
        while (!line.isNull());
    }
}
