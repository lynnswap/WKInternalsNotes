# ``WKInternalsNotes/WKProcessPool/_addSupportedPlugin(_:named:withMimeTypes:withExtensions:)``

対応プラグイン情報をプロセスプールに追加する。

## Objective-C Declaration
```objective-c
- (void)_addSupportedPlugin:(NSString *) domain named:(NSString *) name withMimeTypes: (NSSet<NSString *> *) mimeTypes withExtensions: (NSSet<NSString *> *) extensions WK_API_AVAILABLE(macos(10.14), ios(12.0));
```

## Discussion
MIME type と拡張子の `NSSet` を `HashSet<String>` に変換し、`addSupportedPlugin(domain, name, mimeTypes, extensions)` を呼び出す。

## References
- [`WKProcessPoolPrivate.h#L116`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L116)
- [`WKProcessPool.mm#L366`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L366)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
