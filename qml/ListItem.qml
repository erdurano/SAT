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
            anchors.fill: parent
            anchors.right: done_button.left
            

            Label{
                height: parent.height
                text: "test test tesTfjdkslajf"
                font.family: "Ubuntu Mono"
                font.pixelSize: 12
                color: "black"
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
            }
            
            Label{
                height: parent.height
                text: "test test tesT"
                font.family: "Ubuntu Mono"
                font.pixelSize: 12
                color: "black"
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
            }

            Label{
                height: parent.height
                text: "test test tesT"
                font.family: "Ubuntu Mono"
                font.pixelSize: 12
                color: "black"
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
            }

            Label{
                height: parent.height
                text: "test test tesT"
                font.family: "Ubuntu Mono"
                font.pixelSize: 12
                color: "black"
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
            }

            Label{
                height: parent.height
                text: "test test tesT"
                font.family: "Ubuntu Mono"
                font.pixelSize: 12
                color: "black"
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
            }
        }

        

        RoundButton {
            id: done_button
            height: item_root.height-4
            radius: height/2
            anchors.right: parent.right
            anchors.verticalCenter: parent.verticalCenter
            text: "Done"
            width: text.width + height
            onClicked: console.log("Yippeeeee!")
        }
    }
}