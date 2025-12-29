# ``WKInternalsNotes/WKMouseInteraction/mouseTouch``

現在のマウスタッチを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) UITouch *mouseTouch;
```

## Default Value
`_touching` の状態に応じて `_currentMouseTouch` または `_currentHoverTouch` を返す。

## Discussion
タッチ中は `_currentMouseTouch`、それ以外は `_currentHoverTouch` を返す。

## References
- [`WKMouseInteraction.h#L56`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseInteraction.h#L56)
- [`WKMouseInteraction.mm#L227`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseInteraction.mm#L227)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
