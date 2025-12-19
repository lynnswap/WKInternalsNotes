# ``WKInternalsNotes/WKScrollView/_didChangeTopScrollEdgeEffectStyle()``

トップエッジエフェクトのスタイル変更を内部へ通知する。

## Objective-C Declaration
```objective-c
- (void)_didChangeTopScrollEdgeEffectStyle;
```

## Discussion
内部 delegate が存在する場合に、トップポケット色とハードポケット設定の更新を依頼する。

## References
- [`WKScrollView.h#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.h#L59)
- [`WKScrollView.mm#L704`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.mm#L704)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
