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

        Row {
            id: button_row
            anchors {
                top: list_window.bottom
                bottom: parent.bottom
                left: list_window.left
                right: list_window.right
                topMargin: 5
                bottomMargin: 10
            }

            Button {
                id: dash_btn
                anchors.left: parent.left
                anchors.leftMargin: 3
                text: "Dash It!"
            }

            Button {
                id: imprt_btn
                anchors.right: exprt_btn.left
                anchors.rightMargin: 3
                text: "Import SAT"
            }

            Button {
                id: exprt_btn
                anchors.right: parent.right
                anchors.rightMargin: 3
                text: "Export Dash"

            }
        }
    }
}   