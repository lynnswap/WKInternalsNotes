# ``WKInternalsNotes/WKApplicationStateTrackingView/_applicationWillEnterForeground()``

ページが存在する場合に foreground 遷移を通知し、アクティビティ状態を更新する。

## Objective-C Declaration
```objective-c
- (void)_applicationWillEnterForeground;
```

## Discussion
`_webViewToTrack` から `page` を取得し、存在しなければ何もしない。`page->applicationWillEnterForeground()` を呼んだ後、`activityStateDidChange` を `Immediate`/`Synchronous` で実行する。

## References
- [`WKApplicationStateTrackingView.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKApplicationStateTrackingView.h#L35)
- [`WKApplicationStateTrackingView.mm#L100`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKApplicationStateTrackingView.mm#L100)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
