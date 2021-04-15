import QtQuick 2.2
import QtQuick.Window 2.2
import QtQuick.Controls 2.15

Window{
    id: main_window
    color: "#ffffff"
    height: 480
    width: 640

    Rectangle{
        anchors.fill: parent
        anchors.margins: 15
        anchors.rightMargin: 15 + scroll.width
        anchors.bottomMargin: 50
        border.color: "black"
        border.width: 1

        ListView{
            id: list_window
            anchors.fill: parent
            anchors.topMargin: 3
            anchors.bottomMargin: 3
            spacing: 3
            focus: true
            clip: true


            model : 30
            delegate: ListItem {
                id: index
            }


            ScrollBar.vertical: ScrollBar {
                id: scroll
                parent: list_window.parent
                anchors.top: parent.top
                anchors.left: parent.right
                anchors.bottom: parent.bottom
                policy: ScrollBar.AlwaysOn
                visible:true
            }  
        }
    }
}   