# ``WKInternalsNotes/WKProcessPool/_networkingProcessInfo()``

Network プロセスのタスク情報配列を返す。

## Objective-C Declaration
```objective-c
+ (NSArray<_WKProcessInfo *> *)_networkingProcessInfo WK_API_AVAILABLE(macos(14.5));
```

## Discussion
`NetworkProcessProxy::allNetworkProcesses()` を走査し、taskInfo があれば `_WKProcessInfo` を生成して配列に追加する。

## References
- [`WKProcessPoolPrivate.h#L194`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L194)
- [`WKProcessPool.mm#L697`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L697)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
