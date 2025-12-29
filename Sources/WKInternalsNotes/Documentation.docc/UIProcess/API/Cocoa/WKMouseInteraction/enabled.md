# ``WKInternalsNotes/WKMouseInteraction/enabled``

マウスインタラクションの有効/無効を切り替える。

## Objective-C Declaration
```objective-c
@property (nonatomic, getter=isEnabled) BOOL enabled;
```

## Default Value
`initWithDelegate:` で `YES` に初期化される。

## Discussion
有効状態の変更時にジェスチャの `enabled` を更新し、無効化時はキャッシュ状態をリセットする。

## References
- [`WKMouseInteraction.h#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseInteraction.h#L54)
- [`WKMouseInteraction.mm#L171`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseInteraction.mm#L171)
- [`WKMouseInteraction.mm#L212`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseInteraction.mm#L212)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
