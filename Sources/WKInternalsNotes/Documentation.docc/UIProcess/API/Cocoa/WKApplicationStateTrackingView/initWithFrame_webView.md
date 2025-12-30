# ``WKInternalsNotes/WKApplicationStateTrackingView/initWithFrame(_:webView:)``

`WKWebView` を保持し、`ApplicationStateTracker` を生成して監視を開始する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithFrame:(CGRect)frame webView:(WKWebView *)webView;
```

## Discussion
`[super initWithFrame:]` が失敗した場合は `nil` を返す。`_webViewToTrack` に `webView` を保持し、`_applicationStateTracker` を `ApplicationStateTracker::create` で生成する（`_applicationDidEnterBackground` / `_applicationWillEnterForeground` / `_willBeginSnapshotSequence` / `_didCompleteSnapshotSequence` をコールバックに指定）。

## References
- [`WKApplicationStateTrackingView.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKApplicationStateTrackingView.h#L34)
- [`WKApplicationStateTrackingView.mm#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKApplicationStateTrackingView.mm#L43)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
