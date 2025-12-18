# ``WKInternalsNotes/WKProcessPool/_webContentProcessInfo()``

WebContent プロセスのタスク情報一覧を返す。

## Objective-C Declaration
```objective-c
+ (NSArray<_WKProcessInfo *> *)_webContentProcessInfo WK_API_AVAILABLE(macos(14.5));
```

## Discussion
全プロセスプールと `processes()` を走査し、taskInfo があれば `_WKWebContentProcessInfo` を生成して配列に追加する。

## References
- [`WKProcessPoolPrivate.h#L195`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L195)
- [`WKProcessPool.mm#L709`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L709)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
