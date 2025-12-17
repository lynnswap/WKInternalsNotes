// swift-tools-version: 6.2
// The swift-tools-version declares the minimum version of Swift required to build this package.

import PackageDescription

let package = Package(
    name: "WKInternalsNotes",
    products: [
        // Products define the executables and libraries a package produces, making them visible to other packages.
        .library(
            name: "WKInternalsNotes",
            targets: ["WKInternalsNotes"]
        ),
        .library(
            name: "DocCKindPlayground",
            targets: ["DocCKindPlayground"]
        ),
    ],
    dependencies: [
        .package(url: "https://github.com/apple/swift-docc-plugin.git", from: "1.4.5"),
    ],
    targets: [
        // Targets are the basic building blocks of a package, defining a module or a test suite.
        // Targets can depend on other targets in this package and products from dependencies.
        .target(
            name: "WKInternalsNotes"
        ),
        .target(
            name: "DocCKindPlayground"
        ),
        .testTarget(
            name: "WKInternalsNotesTests",
            dependencies: ["WKInternalsNotes"]
        ),
    ]
)
