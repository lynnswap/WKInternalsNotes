# ``WKInternalsNotes/_WKElementAction/title``

アクションの表示タイトルを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString* title;
```

## Default Value
作成時に設定される（`customTitle` または既定のタイトル）。

## Discussion
初期化時に `title` をコピーして保持し、`title` はその値を返す。

## References
- [`_WKElementAction.h#L70`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKElementAction.h#L70)
- [`_WKElementAction.mm#L90`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKElementAction.mm#L90)
- [`_WKElementAction.mm#L262`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKElementAction.mm#L262)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
