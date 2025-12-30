# ``WKInternalsNotes/WKTextSelectionRect/initWithCGRect(_:)``

矩形から選択ジオメトリを作成して初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithCGRect:(CGRect)rect;
```

## Discussion
`WebCore::SelectionGeometry` を作り、`rect` を `enclosingIntRect` に変換して設定した上で `initWithSelectionGeometry:delegate:` を `delegate:nil` で呼ぶ。

## References
- [`WKTextSelectionRect.h#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKTextSelectionRect.h#L52)
- [`WKTextSelectionRect.mm#L86`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKTextSelectionRect.mm#L86)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
