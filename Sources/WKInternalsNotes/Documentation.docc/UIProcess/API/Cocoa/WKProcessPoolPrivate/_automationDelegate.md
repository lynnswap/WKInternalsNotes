# ``WKInternalsNotes/WKProcessPool/_automationDelegate``

Automation 用 delegate を取得・設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, weak, setter=_setAutomationDelegate:) id <_WKAutomationDelegate> _automationDelegate WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Default Value
未設定の場合は `nil`。

## Discussion
getter は `_automationDelegate` を返す。setter は `_automationDelegate` を更新し、`AutomationClient` を `WebProcessPool` に設定する。

## References
- [`WKProcessPoolPrivate.h#L99`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L99)
- [`WKProcessPool.mm#L327`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L327)
- [`WKProcessPool.mm#L332`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L332)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
