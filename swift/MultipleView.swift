//
//  MultiableViews.swift
//  Testing
//
//  Created by Hugh Quigley on 4/30/24.
//

import SwiftUI

struct MultiableView: View {
    @State private var View = 1
    var body: some View {
        if View == 1 {
            Text("View 1")
                .font(.title)
                .foregroundStyle(.green)
            Spacer()
            HStack {
                Button("View 1") {
                    View = 1
                }
                Button("View 2") {
                    View = 2
                }
                Button("View 3") {
                    View = 3
                }
            }
            .font(.title)
        }
        if View == 2 {
            Text("View 2")
                .font(.title)
                .foregroundStyle(.red)
            Spacer()
            HStack {
                Button("View 1") {
                    View = 1
                }
                Button("View 2") {
                    View = 2
                }
                Button("View 3") {
                    View = 3
                }
            }
            .font(.title)
        }
        if View == 3 {
            Text("View 3")
                .font(.title)
                .foregroundStyle(.blue)
            Spacer()
            HStack {
                Button("View 1") {
                    View = 1
                }
                Button("View 2") {
                    View = 2
                }
                Button("View 3") {
                    View = 3
                }
            }
            .font(.title)
        }
        Spacer()
    }
}

#Preview {
    MultiableView()
}
