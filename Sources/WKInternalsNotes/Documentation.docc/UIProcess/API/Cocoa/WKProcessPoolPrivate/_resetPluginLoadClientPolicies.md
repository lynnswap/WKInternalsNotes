# ``WKInternalsNotes/WKProcessPool/_resetPluginLoadClientPolicies(_:)``

プラグイン読み込みポリシーをリセットする。

## Objective-C Declaration
```objective-c
- (void)_resetPluginLoadClientPolicies:(NSDictionary *)policies WK_API_AVAILABLE(macos(10.13));
```

## Discussion
現在の実装は空で、処理は行わない。

## References
- [`WKProcessPoolPrivate.h#L95`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L95)
- [`WKProcessPool.mm#L305`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L305)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
