# ``WKInternalsNotes/WKPDFPageNumberIndicator/show()``

インジケータをフェードイン表示する。

## Objective-C Declaration
```objective-c
- (void)show;
```

## Discussion
`alpha` をアニメーションで 1 にし、既存タイマーがあれば発火時間を更新する。無ければ `hide:` を呼ぶタイマーを新規作成する。

## References
- [`WKPDFPageNumberIndicator.mm#L154`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/PDF/WKPDFPageNumberIndicator.mm#L154)
- [`WKPDFPageNumberIndicator.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/PDF/WKPDFPageNumberIndicator.h#L40)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
