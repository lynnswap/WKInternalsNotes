# ``WKInternalsNotes/WKWebInspectorPreferenceObserver/sharedInstance()``

Web Inspector 設定監視のシングルトンを返す。

## Objective-C Declaration
```objective-c
+ (id)sharedInstance;
```

## Discussion
`NeverDestroyed` の静的インスタンスを生成して返す。

## References
- [`WebInspectorPreferenceObserver.h#L27`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WebInspectorPreferenceObserver.h#L27)
- [`WebInspectorPreferenceObserver.mm#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WebInspectorPreferenceObserver.mm#L45)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
