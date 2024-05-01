import SwiftUI

struct ContentView: View {
    @State private var Money = 0
    var body: some View {
        Text("Your money is \(Money)")
            .font(.title)
            .bold()
        Spacer()
        Button("Click this to earn money") {
            Money = Money + 1
        }
        .bold()
        .font(.title)
        Spacer()
    }
}

#Preview {
    ContentView()
}
