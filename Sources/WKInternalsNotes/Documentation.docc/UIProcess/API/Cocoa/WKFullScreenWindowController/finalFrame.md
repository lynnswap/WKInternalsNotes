# ``WKInternalsNotes/WKFullScreenWindowController/finalFrame``

フルスクリーン遷移の最終フレーム（画面座標）を保持する。

## Objective-C Declaration
```objective-c
@property (readonly) NSRect finalFrame;
```

## Default Value
初期値は `NSZeroRect`。`beganEnterFullScreenWithInitialFrame:finalFrame:` で設定される。

## Discussion
`finalFrame` は `@synthesize` で `_finalFrame` に束縛され、フルスクリーン開始時に渡されたフレームを保持してアニメーション計算に使われる。

## References
- [`WKFullScreenWindowController.mm#L293`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKFullScreenWindowController.mm#L293)
- [`WKFullScreenWindowController.mm#L467`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKFullScreenWindowController.mm#L467)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
