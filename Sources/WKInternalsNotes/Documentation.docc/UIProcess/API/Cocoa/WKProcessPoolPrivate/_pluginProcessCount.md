# ``WKInternalsNotes/WKProcessPool/_pluginProcessCount()``

プラグインプロセス数を返す。

## Objective-C Declaration
```objective-c
- (size_t)_pluginProcessCount WK_API_AVAILABLE(macos(10.13.4), ios(11.3));
```

## Discussion
現在の実装は 0 を返すのみ。

## References
- [`WKProcessPoolPrivate.h#L142`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L142)
- [`WKProcessPool.mm#L498`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L498)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
