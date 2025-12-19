# ``WKInternalsNotes/WKContentView/_handleSmartMagnificationInformationForPotentialTap(_:renderRect:fitEntireRect:viewportMinimumScale:viewportMaximumScale:nodeIsRootLevel:nodeIsPluginElement:)``

ポテンシャルタップ時のスマート拡大可否を評価する。

## Objective-C Declaration
```objective-c
- (void)_handleSmartMagnificationInformationForPotentialTap:(WebKit::TapIdentifier)requestID renderRect:(const WebCore::FloatRect&)renderRect fitEntireRect:(BOOL)fitEntireRect viewportMinimumScale:(double)viewportMinimumScale viewportMaximumScale:(double)viewportMaximumScale nodeIsRootLevel:(BOOL)nodeIsRootLevel nodeIsPluginElement:(BOOL)nodeIsPluginElement;
```

## Discussion
ポテンシャルタップ中のみ処理し、設定によってはダブルタップよりクリックを優先するかどうかを判定する。要素種別や設定に応じてダブルタップを無効化し、ズーム差分が小さい場合はクリック優先で終了、差分が大きい場合は拡大を待機する。

## References
- [`WKContentViewInteraction.h#L807`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L807)
- [`WKContentViewInteraction.mm#L2707`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L2707)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
