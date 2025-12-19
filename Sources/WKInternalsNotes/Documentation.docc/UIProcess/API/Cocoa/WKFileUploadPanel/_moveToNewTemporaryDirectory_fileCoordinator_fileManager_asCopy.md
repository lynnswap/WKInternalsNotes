# ``WKInternalsNotes/WKFileUploadPanel/_moveToNewTemporaryDirectory(_:fileCoordinator:fileManager:asCopy:)``

一時ディレクトリへファイルを移動/コピーする。

## Objective-C Declaration
```objective-c
+ (WebKit::TemporaryFileMoveResults)_moveToNewTemporaryDirectory:(NSURL *)originalURL fileCoordinator:(NSFileCoordinator *)fileCoordinator fileManager:(NSFileManager *)fileManager asCopy:(BOOL)asCopy;
```

## Discussion
新しい一時ディレクトリを作成し、`NSFileCoordinator` を用いてファイルを移動またはコピーする。結果として移動可否と URL を返す。

## References
- [`WKFileUploadPanel.h#L65`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFileUploadPanel.h#L65)
- [`WKFileUploadPanel.mm#L1362`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFileUploadPanel.mm#L1362)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
