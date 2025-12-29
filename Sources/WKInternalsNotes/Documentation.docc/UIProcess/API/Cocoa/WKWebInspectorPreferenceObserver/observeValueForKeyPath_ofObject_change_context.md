# ``WKInternalsNotes/WKWebInspectorPreferenceObserver/observeValueForKeyPath(_:ofObject:change:context:)``

設定変更に応じてリモートインスペクタを有効化する。

## Objective-C Declaration
```objective-c
- (void)observeValueForKeyPath:(NSString *)keyPath ofObject:(id)object change:(NSDictionary<NSKeyValueChangeKey, id> *)change context:(void *)context;
```

## Discussion
メインランループにディスパッチし、すべての `WebProcessPool` とプロセスに対して `enableRemoteInspectorIfNeeded()` を呼ぶ。

## References
- [`WebInspectorPreferenceObserver.h#L28`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WebInspectorPreferenceObserver.h#L28)
- [`WebInspectorPreferenceObserver.mm#L71`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WebInspectorPreferenceObserver.mm#L71)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
