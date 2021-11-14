import QtQuick
import QtQuick.Layouts

Item {
        property string sfitext // Declare properties here
        property string nameText
        property string clsText
        property string flagText
        property string ownrText
        property string deptText
        property string dateText
        property string hourText
        property string estText
        property string statText
        property string respNameText
        property bool isNear

        id: base
        width:30
        height: 100

    Rectangle {
        id: background
        // color: "#bdc2e8"
        radius: height/8
        border.width: 2
        anchors.fill: parent
        // anchors.rightMargin: 5
        anchors.bottomMargin: 2.5
        // anchors.leftMargin: 5
        anchors.topMargin: 2.5

        
        Text{
            id: sfi
            anchors {
                top: parent.top
                left: parent.left
            }
            width: parent.height*3/4
            height: parent.height
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter

            text: sfitext // And use them here

        }
        
        
        Text {
            id: name
            width: parent.width - sfi.width - stat.width
            height: parent.height/2
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            wrapMode: Text.WordWrap
            font{
                pixelSize: Math.floor(background.height/5)
                weight: Font.Medium
                family: 'Effra'
            }
            anchors {
            top: parent.top
            horizontalCenter: parent.horizontalCenter
            }
            text: nameText // And use them here
        }
        
        
        Text{
            id: cls
            width: (parent.width - parent.height)/6
            y: parent.height*3/4
            anchors {
                left: sfi.right
            }
            text: "C: " + clsText // And use them here
        }
        
        
        Text{
            id: flag
            width: (parent.width - parent.height)/6
            y: parent.height*3/4
            anchors {
                left: cls.right
                }
            text: "F: " + flagText // And use them here
        }
        
        
        Text {
            width: (parent.width - parent.height)/6
            y: parent.height*3/4
            anchors {
                left: flag.right
            }
            text: "O: " + ownrText // And use them here
        }
        
        RowLayout{
            id: resp_layout
            anchors {
                top: parent.verticalCenter
                left: sfi.right
                right: parent.horizontalCenter
            }
            height: parent.height/4


            Text{
                id: dept
                Layout.alignment: Qt.AlignCenter
                text: deptText // And use them here
            }
            
            Text{
                id: resp_name
                text: respNameText

                Layout.alignment: Qt.AlignCenter

            }
        }
        
        Text{
            id: date

            width: (parent.width-parent.height)/2
            height: parent.height/4
            anchors {
                top: parent.verticalCenter
                left: parent.horizontalCenter
            }
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter

            text: dateText // And use them here
        }
        
        
        Text{
            id: startHour
            height: parent.height/4
            anchors {
                right: date.horizontalCenter
                verticalCenter: flag.verticalCenter
                rightMargin:5
            }
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            text: hourText // And use them here
        }
        
        Text{
            height: parent.height/4
            anchors {
                verticalCenter: startHour.verticalCenter
                left: date.horizontalCenter
                leftMargin: 5
            }
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            
            text: estText // And use them here
        }
        
        Text{
            id: stat
            height: parent.height
            width: parent.height*3/4
            wrapMode: Text.WordWrap
            anchors {
                right: parent.right
                top: parent.top    
            }
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            text: statText // And use them here
        }
        
    }

    onStatTextChanged: {
        if (statText == 'Not Started') {
            if (isNear == true) {
                var gradient = near_gradient.createObject(background)
                background.gradient = gradient;
            } else if (isNear == false) {
                var gradient = passive_gradient.createObject(background)
                background.gradient = gradient;
            }
        } else if (statText == 'Active') {
            var gradient = active_gradient.createObject(background)
            background.gradient = gradient;
        } else if (statText == 'Passed') {
            var gradient = passed_gradient.createObject(background)
            background.gradient = gradient;
        } else if (statText == 'Failed') {
            var gradient = failed_gradient.createObject(background)
            background.gradient = gradient;
        }
    }

    onIsNearChanged: {
        console.log(isNear)
        if (statText == 'Not Started') {
            if (isNear == true) {
                var gradient = near_gradient.createObject(background)
                background.gradient = gradient;
            } else if (isNear == false) {
                var gradient = passive_gradient.createObject(background)
                background.gradient = gradient;
            }
        }
    }

    Component{
        id: passive_gradient
        Gradient {
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
    }

    Component{
        id: near_gradient
        Gradient {
            GradientStop {
                position: 0
                color: "#5769cb"
            }

            GradientStop {
                position: 0.01
                color: "#5769cb"
            }

            GradientStop {
                position: 1
                color: "#e6dee9"
            }
        }

    }

    Component{
        id: active_gradient
        Gradient {
            GradientStop {
                position: 0
                color: "#0072CE"
            }

            GradientStop {
                position: 0.01
                color: "#71a8d6"
            }

            GradientStop {
                position: 1
                color: "#e0e9f0"
            }
        }

    }

    Component{
        id: failed_gradient
        Gradient {
            GradientStop {
                position: 0
                color: "#c87979"
            }

            GradientStop {
                position: 0.01
                color: "#c87979"
            }

            GradientStop {
                position: 1
                color: "#e6dee9"
            }
        }

    }

    Component{
        id: passed_gradient
        Gradient {
            GradientStop {
                position: 0
                color: "#88cd7e"
            }

            GradientStop {
                position: 0.01
                color: "#88cd7e"
            }

            GradientStop {
                position: 1
                color: "#e6dee9"
            }
        }

    }

}