# ``WKInternalsNotes/WKContentView/_internalContextMenuInteraction(_:configurationForMenuAtLocation:completion:)``

内部のコンテキストメニュー設定取得フローを実行する。

## Objective-C Declaration
```objective-c
- (void)_internalContextMenuInteraction:(UIContextMenuInteraction *)interaction configurationForMenuAtLocation:(CGPoint)location completion:(void(^)(UIContextMenuConfiguration *))completion;
```

## Discussion
WebView 未設定や長押しアクション無効時は `completion(nil)` で終了する。位置情報更新のリクエストを組み立てて `doAfterPositionInformationUpdate` を実行し、更新後に `continueContextMenuInteraction` へ進む。画像解析待ちが必要な場合は `_doAfterPendingImageAnalysis` 経由で進行する。

## References
- [`WKContentViewInteraction.mm#L1146`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L1146)
- [`WKContentViewInteraction.mm#L14979`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14979)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
