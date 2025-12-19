# ``WKInternalsNotes/WKContentView/_showPlaybackTargetPicker(_:fromRect:routeSharingPolicy:routingContextUID:)``

再生デバイス選択ピッカーを表示する。

## Objective-C Declaration
```objective-c
- (void)_showPlaybackTargetPicker:(BOOL)hasVideo fromRect:(const WebCore::IntRect&)elementRect routeSharingPolicy:(WebCore::RouteSharingPolicy)policy routingContextUID:(NSString *)contextUID;
```

## Discussion
`WKAirPlayRoutePicker` を生成して、指定ポリシーとコンテキストで表示する。

## References
- [`WKContentViewInteraction.h#L828`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L828)
- [`WKContentViewInteraction.mm#L9671`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L9671)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
