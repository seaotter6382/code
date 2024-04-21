import SwiftUI

struct DiffrentView: View {
    @State private var Toggle = false
    var body: some View {
        if Toggle == false {
            Text("Toggle is False")
                .font(.title)
                .foregroundStyle(.red)
            Spacer()
            Button("Toggle View") {
                Toggle.toggle()
            }
        }
        if Toggle == true {
            Text("Toggle is True")
                .font(.title)
                .foregroundStyle(.green)
            Spacer()
            Button("Toggle View") {
                Toggle.toggle()
            }
        }
    }
}

#Preview {
    DiffrentView()
}
