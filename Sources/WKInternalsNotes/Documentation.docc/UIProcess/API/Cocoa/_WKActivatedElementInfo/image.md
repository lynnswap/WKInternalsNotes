# ``WKInternalsNotes/_WKActivatedElementInfo/image``

要素の画像を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) UIImage *image;
```

## Default Value
初期化時に渡された画像（未設定なら `nil`）。

## Discussion
初回アクセス時に `ShareableBitmap` から `UIImage/NSImage` を生成して保持し、以降はそのコピーを返す。

## References
- [`_WKActivatedElementInfo.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.h#L45)
- [`_WKActivatedElementInfo.mm#L243`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.mm#L243)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
