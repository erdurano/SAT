import QtQuick 2.2
import QtQuick.Controls 2.15


Item {
    id: item_root
    width: parent.width - 6
    x: 3
    height: 30

    Rectangle{
        height: parent.height
        width: parent.width
        color: "#f0f0f0"

        Row{
            spacing:3
            height: parent.height
            width: parent.width
            

            Label{
                text: "test test tesT"
                font.family: "Ubuntu Mono"
                font.pointSize: 12
                color: "black"
            }
            
            Label{
                text: "test test tesT"
                font.family: "Ubuntu Mono"
                font.pointSize: 12
                color: "black"
            }

            Label{
                text: "test test tesT"
                font.family: "Ubuntu Mono"
                font.pointSize: 12
                color: "black"
            }

            Label{
                text: "test test tesT"
                font.family: "Ubuntu Mono"
                font.pointSize: 12
                color: "black"
            }

            Label{
                text: "test test tesT"
                font.family: "Ubuntu Mono"
                font.pointSize: 12
                color: "black"
            }

            RoundButton {
                id: done_button
                height: item_root.height-4
                width: 100
                radius: height/2

                text: "Done"
                onClicked: console.log("Yippeeeee!")
            }
        }
    }
}