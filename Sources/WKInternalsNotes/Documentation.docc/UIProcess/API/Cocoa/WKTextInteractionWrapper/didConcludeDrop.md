# ``WKInternalsNotes/WKTextInteractionWrapper/didConcludeDrop()``

ドロップ完了時に edit menu 抑制を解除する。

## Objective-C Declaration
```objective-c
- (void)didConcludeDrop;
```

## Discussion
`_hideEditMenuScope` を破棄し、スコープのデストラクタで edit menu や選択の復元を行う。

## References
- [`WKTextInteractionWrapper.h#L62`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.h#L62)
- [`WKTextInteractionWrapper.mm#L350`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L350)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
