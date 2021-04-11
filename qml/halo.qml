import QtQuick 2.0

Item {
    id: test_item_ui
    width: list_window.width
    height: 100
    property alias status: status
    property alias department_label: department_label
    property alias date_str_label: date_str_label
    property alias test_label: test_label
    property alias sfi_label: sfi_label.text
    property alias cls_presence: cls_presence
    property alias ownr_presence: ownr_presence
    property alias flg_presence: flg_presence

    Rectangle {
        id: rectangle
        color: "#bdc2e8"
        radius: parent.height/2
        border.width: 2
        anchors.fill: parent
        anchors.rightMargin: 0
        anchors.bottomMargin: 0
        anchors.leftMargin: 0
        anchors.topMargin: 0
        gradient: Gradient {
            GradientStop {
                position: 0
                color: "#bdc2e8"
            }

            GradientStop {
                position: 0.01
                color: "#bdc2e8"
            }

            GradientStop {
                position: 1
                color: "#e6dee9"
            }
        }

        Text {
            id: test_label
            x: 83
            y: 8
            width: 98
            height: 51
            text: "test name"
            font.pixelSize: 12
            verticalAlignment: Text.AlignVCenter
            wrapMode: Text.WordWrap
            fontSizeMode: Text.VerticalFit
        }

        Text {
            id: sfi_label
            x: 30
            y: 42
            text: qsTr("SFI")
            font.pixelSize: 12
        }

        Text {
            id: date_str_label
            x: 101
            y: 58
            text: qsTr("Text")
            font.pixelSize: 12
        }

        Text {
            id: cls_presence
            x: 306
            y: 50
            width: 24
            height: 32
            text: qsTr("Text")
            font.pixelSize: 12
            horizontalAlignment: Text.AlignHCenter
            wrapMode: Text.WordWrap
            maximumLineCount: 2
        }

        Text {
            id: flg_presence
            x: 375
            y: 50
            width: 24
            height: 32
            text: qsTr("Text")
            font.pixelSize: 12
            horizontalAlignment: Text.AlignHCenter
            wrapMode: Text.WordWrap
            maximumLineCount: 2
        }

        Text {
            id: ownr_presence
            x: 443
            y: 50
            width: 24
            height: 32
            text: qsTr("Text")
            font.pixelSize: 12
            horizontalAlignment: Text.AlignHCenter
            wrapMode: Text.WordWrap
            maximumLineCount: 2
        }

        Text {
            id: department_label
            x: 306
            y: 19
            width: 161
            height: 17
            text: qsTr("Text")
            font.pixelSize: 12
        }

        Text {
            id: status
            x: 537
            y: 42
            text: qsTr("status")
            font.pixelSize: 12
        }
    }




}
