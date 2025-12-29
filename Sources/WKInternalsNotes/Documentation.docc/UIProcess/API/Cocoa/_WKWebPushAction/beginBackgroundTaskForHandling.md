# ``WKInternalsNotes/_WKWebPushAction/beginBackgroundTaskForHandling()``

Web Push 処理用のバックグラウンドタスクを開始する（iOS のみ）。

## Objective-C Declaration
```objective-c
- (UIBackgroundTaskIdentifier)beginBackgroundTaskForHandling;
```

## Discussion
iOS では `_nameForBackgroundTaskAndLogging` からタスク名を構築し、`webClipIdentifier` がある場合はそれを付加して `UIApplication` に渡す。期限切れ時はログを出力する。iOS 以外では `0` を返す。

## References
- [`_WKWebPushAction.mm#L129`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushAction.mm#L129)
- [`_WKWebPushAction.h#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushAction.h#L49)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
