import QtQuick 2.2
import QtQuick.Window 2.2

Window{
    id: main_window
    color: "#ffffff"
    height: 480
    width: 640

    Rectangle{
        anchors.fill: parent
        anchors.margins: 10
        anchors.bottomMargin: 50
        border.color: "black"
        border.width: 1
        ListView{
            id: list_window
            anchors.fill: parent
            spacing: 3
            clip: true

            Repeater{
                model: [0, 1, 2, 3, ,4 ,5 ,6 ,7 ,8, 9, 10, 11, 12]
                clip: true
                Halo{
                    id: modelitem
                }
            }
        }
    }
}   