# ``WKInternalsNotes/_WKDownload/downloadWithDownload(_:)``

`WKDownload` をラップした `_WKDownload` を取得する。

## Objective-C Declaration
```objective-c
+ (instancetype)downloadWithDownload:(WKDownload *)download WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
内部の `NSMapTable` で `WKDownload` と `_WKDownload` の弱参照マップを管理し、既存ラッパーがあればそれを返す。未登録の場合は `initWithDownload2:` で生成してマップへ登録する。

## References
- [`_WKDownload.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownload.h#L36)
- [`_WKDownload.mm#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownload.mm#L41)
- [`_WKDownload.mm#L64`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownload.mm#L64)
- [`_WKDownload.mm#L66`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownload.mm#L66)
- [`_WKDownload.mm#L68`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownload.mm#L68)
- [`_WKDownload.mm#L69`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownload.mm#L69)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
