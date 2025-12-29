# ``WKInternalsNotes/WKAirPlayRoutePicker/showFromView(_:routeSharingPolicy:routingContextUID:hasVideo:)``

AirPlay ルート選択 UI を表示する。

## Objective-C Declaration
```objective-c
- (void)showFromView:(UIView *)view routeSharingPolicy:(WebCore::RouteSharingPolicy)policy routingContextUID:(NSString *)contextUID hasVideo:(BOOL)hasVideo;
```

## Discussion
既に表示中の場合は何もしない。`MPAVRoutingController` を作成して探索モードを有効化し、`hasVideo` に応じてルート並び替え設定を行った `MPMediaControlsViewController` を生成する。対応環境では `routeSharingPolicy` と `routingContextUID` を上書きし、閉じたときに探索を停止して状態をクリアする。最後に `view` の全画面プレゼンテーション用 `UIViewController` から表示する。

## References
- [`WKAirPlayRoutePicker.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKAirPlayRoutePicker.h#L37)
- [`WKAirPlayRoutePicker.mm#L72`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKAirPlayRoutePicker.mm#L72)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
