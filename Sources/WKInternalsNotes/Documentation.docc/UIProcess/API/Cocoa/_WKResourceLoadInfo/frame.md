# ``WKInternalsNotes/_WKResourceLoadInfo/frame``

読み込み元のフレームハンドルを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) _WKFrameHandle *frame;
```

## Default Value
未調査（初期化経路の確認が必要）。

## Discussion
`frameID` が存在する場合に `_WKFrameHandle` を生成して返し、無ければ `nil`。

## References
- [`_WKResourceLoadInfo.h#L57`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKResourceLoadInfo.h#L57)
- [`_WKResourceLoadInfo.mm#L92`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKResourceLoadInfo.mm#L92)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
