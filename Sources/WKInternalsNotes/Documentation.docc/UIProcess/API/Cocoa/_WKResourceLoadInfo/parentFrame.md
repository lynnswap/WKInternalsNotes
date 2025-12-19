# ``WKInternalsNotes/_WKResourceLoadInfo/parentFrame``

親フレームのハンドルを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, nullable) _WKFrameHandle *parentFrame;
```

## Default Value
未調査（初期化経路の確認が必要）。

## Discussion
`parentFrameID` が存在する場合に `_WKFrameHandle` を生成して返し、無ければ `nil`。

## References
- [`_WKResourceLoadInfo.h#L58`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKResourceLoadInfo.h#L58)
- [`_WKResourceLoadInfo.mm#L99`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKResourceLoadInfo.mm#L99)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
