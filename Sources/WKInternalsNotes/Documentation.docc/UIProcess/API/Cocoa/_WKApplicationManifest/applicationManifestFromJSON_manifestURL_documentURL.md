# ``WKInternalsNotes/_WKApplicationManifest/applicationManifestFromJSON(_:manifestURL:documentURL:)``

JSON 文字列からマニフェストを生成する。

## Objective-C Declaration
```objective-c
+ (_WKApplicationManifest *)applicationManifestFromJSON:(NSString *)json manifestURL:(nullable NSURL *)manifestURL documentURL:(nullable NSURL *)documentURL;
```

## Discussion
`ApplicationManifestParser::parse` で解析し、`API::ApplicationManifest` の wrapper を返す。

## References
- [`_WKApplicationManifest.h#L102`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.h#L102)
- [`_WKApplicationManifest.mm#L351`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.mm#L351)
- [`_WKApplicationManifest.mm#L353`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.mm#L353)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
