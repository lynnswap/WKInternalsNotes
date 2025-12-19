# ``WKInternalsNotes/WKPageHostedModelView/shouldDisablePortal``

ポータル挙動を無効化するかを設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL shouldDisablePortal;
```

## Discussion
設定変更時に、ステレオコンテンツ有効ならエンティティ/レイヤ構成を切り替える。通常時は `separatedOptions.isPortal` と `separatedOptions.updates.clippingPrimitive` を切り替える。

## References
- [`WKPageHostedModelView.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKPageHostedModelView.h#L36)
- [`WKPageHostedModelView.mm#L220`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKPageHostedModelView.mm#L220)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
