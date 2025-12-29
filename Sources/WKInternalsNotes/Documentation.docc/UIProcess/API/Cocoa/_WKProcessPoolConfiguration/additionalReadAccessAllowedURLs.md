# ``WKInternalsNotes/_WKProcessPoolConfiguration/additionalReadAccessAllowedURLs``

WebContent が追加で読み取れるファイル URL の一覧を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) NSArray<NSURL *> *additionalReadAccessAllowedURLs WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Default Value
未設定時は空配列を返す。

## Discussion
getter は `additionalReadAccessAllowedPaths` を `file://` URL に変換して返し、空なら `@[]` を返す。setter は file URL 以外を拒否して `NSInvalidArgumentException` を投げ、`fileSystemRepresentation` を内部パスとして保存する。

## References
- [`_WKProcessPoolConfiguration.mm#L140`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L140)
- [`_WKProcessPoolConfiguration.mm#L151`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L151)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
