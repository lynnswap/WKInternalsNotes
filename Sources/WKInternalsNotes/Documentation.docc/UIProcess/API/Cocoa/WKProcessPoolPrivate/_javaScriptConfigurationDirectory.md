# ``WKInternalsNotes/WKProcessPool/_javaScriptConfigurationDirectory``

JavaScript 設定ディレクトリの URL を取得・設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy, setter=_setJavaScriptConfigurationDirectory:) NSURL *_javaScriptConfigurationDirectory WK_API_AVAILABLE(macos(10.15.4), ios(13.4));
```

## Default Value
`_processPool->javaScriptConfigurationDirectory()` のパスを `fileURLWithPath:isDirectory:` で URL 化した値。

## Discussion
getter は `WebProcessPool` の設定ディレクトリをファイル URL に変換して返す。setter は `file://` 以外の URL を `NSInvalidArgumentException` で拒否し、`setJavaScriptConfigurationDirectory` に path を渡す。

## References
- [`WKProcessPoolPrivate.h#L115`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L115)
- [`WKProcessPool.mm#L354`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L354)
- [`WKProcessPool.mm#L354`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L354)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
