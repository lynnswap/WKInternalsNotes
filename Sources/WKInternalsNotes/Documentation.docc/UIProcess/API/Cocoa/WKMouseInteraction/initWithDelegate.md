# ``WKInternalsNotes/WKMouseInteraction/initWithDelegate(_:)``

マウス関連のジェスチャー認識器を初期化して初期状態を設定する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithDelegate:(id <WKMouseInteractionDelegate>)delegate;
```

## Discussion
`WKMouseTouchGestureRecognizer` と 2 種類の `UIHoverGestureRecognizer` を生成し、delegate 設定・許可タッチタイプ設定・名前付けを行う。`delegate` を保持し、`enabled = YES`、`_cancelledOrExited = YES` で初期化する。

## References
- [`WKMouseInteraction.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseInteraction.h#L44)
- [`WKMouseInteraction.mm#L150`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseInteraction.mm#L150)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
