# ``WKInternalsNotes/_WKApplicationManifest/initWithJSONData(_:manifestURL:documentURL:)``

JSON データからアプリケーションマニフェストを生成する。

## Objective-C Declaration
```objective-c
- (nullable instancetype)initWithJSONData:(NSData *)jsonData manifestURL:(NSURL *)manifestURL documentURL:(NSURL *)documentURL WK_API_AVAILABLE(macos(14.5), ios(17.5), visionos(1.2));
```

## Discussion
JSON を UTF-8 文字列に変換し、`ApplicationManifestParser::parseWithValidation` で検証付き解析を行う。変換や解析に失敗した場合は `nil` を返す。

## References
- [`_WKApplicationManifest.h#L73`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.h#L73)
- [`_WKApplicationManifest.mm#L244`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.mm#L244)
- [`_WKApplicationManifest.mm#L253`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.mm#L253)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
