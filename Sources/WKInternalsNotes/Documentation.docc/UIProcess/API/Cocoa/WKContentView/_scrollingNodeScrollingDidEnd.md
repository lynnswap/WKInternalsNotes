# ``WKInternalsNotes/WKContentView/_scrollingNodeScrollingDidEnd(_:)``

スクロールノードのスクロール終了を処理する。

## Objective-C Declaration
```objective-c
- (void)_scrollingNodeScrollingDidEnd:(std::optional<WebCore::ScrollingNodeID>)nodeID;
```

## Discussion
選択コンテナのスクロール終了時はエディタ状態更新をスケジュールし、必要なら選択復元を遅延する。更新可能な場合は選択更新とオーバーフロースクロール終了通知を行い、`WKWebView` へ終了を通知する。

## References
- [`WKContentViewInteraction.h#L827`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L827)
- [`WKContentViewInteraction.mm#L2772`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L2772)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
