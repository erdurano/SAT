import QtQuick 2.0
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.1

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "QML Listview Demo"

    ListView {
        clip: true
        anchors.fill: parent
        anchors.margins: 5
        spacing: 5

        delegate: listDelegate
        
        Component {
            id: listDelegate

            RowLayout {
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.margins: 10
                spacing: 10

                CheckBox {}
                Label { text: itemType; color: "#888" ; font.italic: true }
                Label { text: itemName; Layout.fillWidth: true }
                Label { text: itemPath }
                ComboBox { model: itemVersions; Layout.preferredWidth: 90 }
            }
        }

        model: mymodel
        // model: ListModel {
            
        //     ListElement {
        //         itemType: "asset"
        //         itemName: "First entry"
        //         itemPath: "/documents/fe.md"
        //         itemVersions: []
        //     }
        //     ListElement {
        //         itemType: "asset"
        //         itemName: "Second entry"
        //         itemPath: "/documents/se.md"
        //         itemVersions: []
        //     }
        //     ListElement {
        //         itemType: "asset"
        //         itemName: "Third entry"
        //         itemPath: "/documents/te.md"
        //         itemVersions: []
        //     }
        // }
    }
}